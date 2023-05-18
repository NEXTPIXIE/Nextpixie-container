from datetime import datetime, timedelta
from django.utils import timezone


def is_otp_expired(created_time: timezone) -> bool:

    """OTP Validator"""
    current_time = timezone.now()
    created_datetime = timezone.make_aware(datetime.combine(current_time.date(), created_time))
    
    expiry_time = created_datetime + timedelta(seconds=300)
    if current_time < expiry_time:
        return False
    else:
        return True

