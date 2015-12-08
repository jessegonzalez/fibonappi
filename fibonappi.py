from flask import Flask
from flask_restplus import Api, Resource

VERSION = '0.1.0'

app = Flask(__name__)
api = Api(app, version=VERSION, title='Fibonacci Sequence API',
          description='An API that returns the first n integers of the Fibonacci Sequence.',
          validate=True
          )

ns = api.namespace('fibonacci', description='fibonacci operation')


@ns.route('/<path:input>')
@api.response(200, 'Success - sequence returned')
@api.response(400, 'Invalid Input')
@api.doc(params={'input': 'The count of Fibonacci sequence numbers to return.'})
class Fibonappi(Resource):
    '''Get the desired count of numbers in the Fibonacci sequence.'''

    def abort_if_non_int(self, input):
        try:
            return int(input)
        except ValueError:
            api.abort(400, 'Invalid input {}. Integer required.'.format(input))

    def abort_on_negative(self, number):
        if number < 0:
            api.abort(400, "The number {} does not work for the Fibonacci sequence.".format(number))

    def fib(self, n, a=0, b=1):
        while n > 0:
            yield a
            a, b, n = b, a + b, n - 1

    @api.doc(description='number should be greater than 0')
    def get(self, input):
        '''Calculate the Fibonacci sequence'''
        number = self.abort_if_non_int(input)
        self.abort_on_negative(number)
        return [i for i in self.fib(number)]


if __name__ == '__main__':
    app.run(debug=True)
