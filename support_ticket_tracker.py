"""Simple support ticket tracker."""
import json
import logging
TICKETS = {}


def create_ticket(title, description, reporter,
                  priority="medium", category="general"):
    """Create a new ticket and add it to the tracker."""
    if not title:
        return None
    ticket_id = str(len(TICKETS) + 1)
    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "status": "open",
        "reporter": reporter,
        "assignee": None
        }
    audit_log = []
    TICKETS[ticket_id] = ticket
    audit_log.append(f"Created ticket {ticket_id} for {reporter}")
    return ticket


def assign_ticket(ticket_id, agent):
    """Assign a ticket to an agent. Return True on success."""
    try:
        TICKETS[ticket_id]["assignee"] = agent
        return True
    except KeyError:
        return False


def update_status(ticket_id, status):
    """Set a ticket's status and return the ticket."""
    TICKETS[ticket_id]["status"] = status
    return TICKETS[ticket_id]


def search_tickets(status=None, priority=None):
    """Return tickets matching the given status and priority."""
    r = []
    for t in TICKETS.values():
        if status is not None and t["status"] != status:
            continue
        if priority and t["priority"] != priority:
            continue
        r.append(t)
    return r


def save_tickets(path="tickets.json"):
    """Save all tickets to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(TICKETS, file)


def load_tickets(path="tickets.json"):
    """Load tickets from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    TICKETS.clear()
    TICKETS.update(data)


def print_ticket_report():
    """Print a summary of all tickets."""
    print("Support Tickets")
    if not TICKETS:
        print("No tickets yet")
    for ticket_id, ticket in TICKETS.items():
        print(ticket_id, ticket["title"], ticket["status"])


def close_ticket(ticket_id):
    """Mark a ticket as closed."""
    TICKETS[ticket_id]["status"] = "closed"


def is_open(ticket_id):
    """Mark a ticket as open."""
    status = TICKETS[ticket_id]["status"]
    return status in ("open", "in_progress")


def main():
    """Run a demo of the ticket tracker."""
    logging.basicConfig(level=logging.INFO)
    create_ticket("Cannot sign in", "Password reset link fails",
                  "alex@example.com")
    create_ticket("Billing question", "Charged twice",
                  "lee@example.com", "high")
    assign_ticket("1", "agent-01")
    update_status("1", "in_progress")
    print_ticket_report()
    logging.info("Tickets created: %d", len(TICKETS))
    print("Ticket 1 open?", is_open("1"))
    ticket_id = input("Ticket id to close (Enter to skip): ")
    if ticket_id:
        close_ticket(ticket_id)
    save_tickets()


if __name__ == "__main__":
    main()
