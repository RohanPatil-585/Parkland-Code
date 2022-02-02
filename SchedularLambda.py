def lambda_handler(event, context):
            message = "Hello Lambda World!!!"
            logger.info('Message ==>> ' + message)
            return message