import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import urllib.parse
import pytz

class TimezoneHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<form action="/get_timezone" method="get">')
            self.wfile.write(b'Timezone: <input type="text" name="timezone"><br>')
            self.wfile.write(b'<input type="submit" value="Submit">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
        elif parsed_path.path == '/get_timezone':
            if 'timezone' in query:
                user_timezone = query['timezone'][0]
                try:
                    user_tz = pytz.timezone(user_timezone)
                    utc_time = datetime.datetime.now(pytz.utc)
                    user_time = utc_time.astimezone(user_tz)
                    response = f"Time in {user_timezone} is {user_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
                except Exception as e:
                    response = f"Invalid timezone provided: {str(e)}"
            else:
                response = "No timezone provided."
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()

def start_server():
    PORT = 8080
    with HTTPServer(("0.0.0.0", PORT), TimezoneHandler) as httpd:
        print(f"Listening on port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    server_thread.join()

