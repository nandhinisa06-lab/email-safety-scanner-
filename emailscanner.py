import re

def scan_email(email_text):
    flags = []

    # Convert to lowercase for easy checking
    text = email_text.lower()

    # Suspicious keywords
    urgent_keywords = ["urgent", "immediately", "action required", "verify now", "limited time"]
    sensitive_keywords = ["password", "otp", "bank details", "credit card", "account"]

    # Check urgent requests
    if any(word in text for word in urgent_keywords):
        flags.append("Contains urgent/suspicious request")

    # Check sensitive data prompts
    if any(word in text for word in sensitive_keywords):
        flags.append("Requests sensitive information")

    # Check links
    links = re.findall(r"http[s]?://\S+", email_text)
    if links:
        flags.append(f"Contains suspicious link(s): {links}")

    # Final result
    print("\n--- Email Safety Report ---")
    if flags:
        print("⚠️ WARNING: Potentially Unsafe Email Detected!\n")
        for f in flags:
            print("-", f)
    else:
        print("✅ Safe Email - No suspicious patterns found.")

# Input email content
email = input("Paste email content: ")
scan_email(email)