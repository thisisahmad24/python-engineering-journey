import json

FILE = "logs.json"


def load_logs():
    with open(FILE, "r") as f:
        return json.load(f)


# Count actions per user
def user_activity():
    logs = load_logs()
    activity = {}

    for log in logs:
        user = log["user"]
        activity[user] = activity.get(user, 0) + 1

    return activity


# Most active user
def most_active():
    activity = user_activity()
    return max(activity, key=activity.get)


# Action count
def action_count():
    logs = load_logs()
    actions = {}

    for log in logs:
        act = log["action"]
        actions[act] = actions.get(act, 0) + 1

    return actions


# Detect suspicious (too many actions)
def detect_suspicious(threshold=3):
    activity = user_activity()

    suspicious = [user for user, count in activity.items() if count > threshold]

    return suspicious


# Insights
def insights():
    activity = user_activity()
    actions = action_count()

    print("Most active user:", most_active())
    print("User activity:", activity)
    print("Action breakdown:", actions)

    sus = detect_suspicious()
    if sus:
        print(" Suspicious users:", sus)
    else:
        print(" No suspicious activity")