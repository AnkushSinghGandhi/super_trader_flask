from flask import jsonify
from app.shared.models.last_quote_array import LastQuoteArrayModel
from app.shared.models.last_quote_option_greek_chain import LastQuoteOptionChainModel

class OptionDashboardController:
    @staticmethod
    def get_straddle_data():
        results = []

        option_chain = LastQuoteOptionChainModel.get_live_option_chain()

        for quote in option_chain:
            call_ltp = ''
            pe_ltp = ''
            instrument_identifier = quote["InstrumentIdentifier"]

            # Extracting strike price from instrument identifier
            strike_price = float(instrument_identifier.split("_")[-1])

            # Getting the last trade price from last quote array
            last_trade_price = LastQuoteArrayModel.get_last_trade_price(instrument_identifier.split("_")[1] + '-I')

            # Checking if it's a call or put option
            if 'CE' in instrument_identifier:
                call_ltp = quote['LastTradePrice']
            else:
                pe_ltp = quote['LastTradePrice']

            if 'PE' in instrument_identifier:
                pe_ltp = quote['LastTradePrice']
            else:
                pe_ltp = call_ltp

            # Handling cases where last trade price is 0 or empty
            if last_trade_price == 0 or last_trade_price == '':
                last_trade_price = 1
            if call_ltp == 0 or call_ltp == '':
                call_ltp = pe_ltp
            if pe_ltp == 0 or pe_ltp == '':
                pe_ltp = call_ltp

            # Calculating the straddle value
            straddle_value = ((float(call_ltp) + float(pe_ltp)) / strike_price) * 100

            result = {
                "InstrumentIdentifier": instrument_identifier,
                "IV": quote["IV"],
                "straddle_value": straddle_value
            }
            results.append(result)

        return jsonify(results)

    @staticmethod
    def get_option_dashboard_data():
        results = []

        option_chain = LastQuoteOptionChainModel.get_live_option_chain()

        for quote in LastQuoteArrayModel.get_last_quote_array():
            symbol = quote["InstrumentIdentifier"]
            liquidity = quote["TotalQtyTraded"]
            ltp = quote["LastTradePrice"]
            change_percentage = quote["PriceChangePercentage"]

            atm_ce_ltp = None
            atm_pe_ltp = None
            call_iv = None
            put_iv = None
            closest_strike = None
            closest_instrument_identifier = None
            closest_strike_diff = float('inf')

            for record in option_chain:
                instrument_identifier = record["InstrumentIdentifier"]
                if symbol.replace("-I", "") in instrument_identifier:
                    strike_price = float(instrument_identifier.split("_")[-1])
                    underlying_ltp = float(record["LastTradePrice"])

                    diff = abs(strike_price - underlying_ltp)

                    if diff < closest_strike_diff:
                        closest_strike_diff = diff
                        closest_strike = strike_price
                        closest_instrument_identifier = instrument_identifier

                    if closest_instrument_identifier is not None and closest_strike is not None:
                        if closest_instrument_identifier.replace("-I", "") in record['InstrumentIdentifier']:
                            if "CE" in record["InstrumentIdentifier"]:
                                call_iv = record['IV']
                                atm_ce_ltp = record['LastTradePrice']

                                record_put_iv = LastQuoteOptionChainModel.get_live_option_chain(
                                    {"InstrumentIdentifier": record["InstrumentIdentifier"].replace("CE", "PE")})
                                for elem in record_put_iv:
                                    put_iv = elem['IV']
                                    atm_pe_ltp = elem['LastTradePrice']
                                    break

                            elif "PE" in record["InstrumentIdentifier"]:
                                put_iv = record['IV']
                                atm_pe_ltp = record['LastTradePrice']

                                record_ce_iv = LastQuoteOptionChainModel.get_live_option_chain(
                                    {"InstrumentIdentifier": record["InstrumentIdentifier"].replace("PE", "CE")})
                                for elem in record_ce_iv:
                                    call_iv = elem['IV']
                                    atm_ce_ltp = elem['LastTradePrice']
                                    break

                            straddle = ((atm_ce_ltp + atm_pe_ltp) / ltp) * 100
                            IV = (call_iv + put_iv) / 2

                            result = {
                                "instrument_identifier": instrument_identifier,
                                "liquidity": liquidity,
                                "symbol": symbol,
                                "ltp": ltp,
                                "change_percentage": change_percentage,
                                "straddle_value": straddle,
                                "ce_iv": call_iv,
                                "pe_iv": put_iv,
                                "IV": IV,
                            }
                            results.append(result)

        return jsonify(results)
