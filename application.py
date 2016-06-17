import os

from sixpack.web import app

port = int(os.environ.get('SIXPACK_PORT', 5001))
debug = 'SIXPACK_DEBUG' in os.environ

application = app

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=port, debug=debug)
