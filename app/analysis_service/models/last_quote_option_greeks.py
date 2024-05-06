from config import db

collection = db["last_quote_option_greeks"]


class QuoteOptionGreeksModel:
    @staticmethod
    def get_iv_data():
        quotes = collection.find()

        results = []
        for quote in quotes:
            Token = quote["Token"]
            iv = quote["IV"]
            results.append(
                {
                    "iv": iv,
                    "Token": Token,
                }
            )

        return results


