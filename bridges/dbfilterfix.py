import logging
from odoo.http import Root, db_filter, db_monodb
_logger = logging.getLogger(__name__)

# allow use of localhost when using dbfilter for report rendereing
def setup_db(self, httprequest):
    db = httprequest.session.db
    # Check if session.db is legit
    if db:
        if db not in db_filter([db], httprequest=httprequest) and  httprequest.environ.get('HTTP_HOST', '').split(':')[0]<>'localhost':
            _logger.warn("Logged into database '%s', but dbfilter "
                         "rejects it as request is %s; logging session out.", db,httprequest.environ.get('HTTP_HOST', ''))
            httprequest.session.logout()
            db = None

    if not db:
        httprequest.session.db = db_monodb(httprequest)
        
Root.setup_db=setup_db
