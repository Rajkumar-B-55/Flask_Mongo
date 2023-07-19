import datetime as dt

import bcrypt
import dateutil.parser as dtp
import pytz


def encode_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def validate_password(incoming_password, hashed_password):
    try:
        return bcrypt.checkpw(incoming_password.encode('utf-8'), hashed_password)
    except Exception as e:
        import traceback
        return False


def dt_from_string(dt_str: str, tz=pytz.utc):
    if not dt_str:
        return None
    datetime = dtp.parse(dt_str)
    udatetime = add_tz(datetime, tz=tz)
    return udatetime


def date_from_string(dt_str: str, tz=pytz.utc):
    dtm = dt_from_string(dt_str, tz)
    date = date_from_dt(dtm)
    return date


def date_from_dt(datetime: dt.datetime):
    return datetime.date() if datetime else None


def add_tz(datetime: dt.datetime, tz=pytz.utc):
    udatetime = datetime.replace(tzinfo=tz)
    return udatetime
