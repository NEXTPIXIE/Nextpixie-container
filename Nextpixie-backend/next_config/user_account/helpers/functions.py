from datetime import datetime, timedelta
from django.utils import timezone


def is_otp_expired(created_time: timezone) -> bool:
    """OTP Validator"""

    current_time = timezone.now()
    expiry_time = created_time + timedelta(seconds=300)
    if current_time < expiry_time:
        return True
    else:
        return False

