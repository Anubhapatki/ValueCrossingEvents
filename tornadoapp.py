import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, Application
from tornado_http_auth import BasicAuthMixin
from crossingevents.ValueCrossingEvents.crossingEvents import CrossingEvents

#credentials = {'apiuser1': 'password'}
class MainHandler(RequestHandler):
   # def prepare(self):
    #    self.get_authenticated_user(check_credentials_func=credentials.get, realm='Protected')

    def get(self):
        value = int(self.get_argument('value'))
        signal = self.get_argument('signal')
        signal = [int(sig) for sig in signal.split(',')]
        print (signal)
        sum = CrossingEvents(signal, value).get_number_of_value_crossings()
        self.write({'sum_of_crossing_events': sum})


def main():
    application = Application([(r'/', MainHandler)], debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()