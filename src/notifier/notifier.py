from src.utils.time_utils import get_timestamp, get_elapsed_time
from src.notifier.whatsapp_sender import send_whatsapp_message

time_holder = []


def notify_message(payload):
    if not payload.get("blink_detected"):
        return  # only handle true blinks

    timestamp = payload["timestamp"]
    time_holder.append(timestamp)
    if len(time_holder) == 3:
        elapse_time = get_elapsed_time(time_holder[0], time_holder[2]).total_seconds()
        if elapse_time < 3:
            send_whatsapp_message("I need something")

            time_holder.clear()
        else:
            elapse_time = get_elapsed_time(time_holder[0], get_timestamp())
            if elapse_time >= 1:
                time_holder.pop(0)
