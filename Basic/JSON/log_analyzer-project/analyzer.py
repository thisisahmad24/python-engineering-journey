import json

FILE = "logs.json"


# Load Logs
def load_logs():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


# Convert time "HH:MM" → minutes
def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


# Count user activity
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


# Action breakdown
def action_count():
    logs = load_logs()
    actions = {}

    for log in logs:
        act = log["action"]
        actions[act] = actions.get(act, 0) + 1

    return actions


# Detect suspicious users
def detect_suspicious(threshold=3):
    activity = user_activity()
    return [user for user, count in activity.items() if count > threshold]


# SESSION TRACKING
def session_durations():
    logs = load_logs()
    sessions = {}
    active_sessions = {}

    for log in logs:
        user = log["user"]
        action = log["action"]
        time = to_minutes(log["time"])

        if action == "login":
            active_sessions[user] = time

        elif action == "logout":
            if user in active_sessions:
                start = active_sessions.pop(user)
                duration = time - start

                sessions[user] = sessions.get(user, [])
                sessions[user].append(duration)

    return sessions


# Total time per user
def total_time_spent():
    sessions = session_durations()
    total_time = {}

    for user, times in sessions.items():
        total_time[user] = sum(times)

    return total_time


# Incomplete sessions
def incomplete_sessions():
    logs = load_logs()
    active = {}

    for log in logs:
        user = log["user"]
        action = log["action"]

        if action == "login":
            active[user] = log["time"]

        elif action == "logout":
            active.pop(user, None)

    return active


# Full Insights
def advanced_insights():
    print("\n=== BASIC ANALYTICS ===")
    print("User activity:", user_activity())
    print("Most active user:", most_active())
    print("Action breakdown:", action_count())

    print("\n=== SESSION ANALYSIS ===")
    sessions = session_durations()
    totals = total_time_spent()
    incomplete = incomplete_sessions()

    print("\nSession durations:")
    for user, times in sessions.items():
        print(user, "→", times)

    print("\nTotal time spent:")
    for user, total in totals.items():
        print(user, "→", total, "minutes")

    if incomplete:
        print("\nIncomplete sessions:")
        print(incomplete)
    else:
        print("\nAll sessions closed properly")