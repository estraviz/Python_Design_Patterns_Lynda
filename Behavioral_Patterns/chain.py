class Handler:
    """ Abstract Handler """

    def __init__(self, successor):
        # Define who is the next Handler or successor if the current Handler is not able to handle the request
        # We need an attribute to store the successor Handler
        self._successor = successor

    def handle(self, request):
        # If handled, stop here
        handled = self._handle(request)

        # Otherwise, keep going
        if not handled:
            self._successor._handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandler1(Handler):
    """ Concrete Handler 1: Inherits from the Abstract Handler """

    def _handle(self, request):
        # Provide a condition for handling
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))

            # This indicates that the request has been handled
            return True


class DefaultHandler(Handler):
    """ Default Handler: Inherits from the Abstract Handler """

    def _handle(self, request):
        """ If there is no handler available """

        # No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))

        # This indicates that the request has been handled
        return True


class Client:
    """ Using handlers """

    def __init__(self):
        # Create handlers and use them in a sequence you want. The default handler has no successor
        self.handler = ConcreteHandler1(DefaultHandler(successor=None))

    def delegate(self, requests):
        # Send your requests one at a time for handlers to handlers
        for request in requests:
            self.handler.handle(request)


# Create a Client
myClient = Client()

# We have to provide the request in the form of a list: we create requests
requests = [4, 8, 15, 16, 23, 42]

# Send the requests
myClient.delegate(requests)
