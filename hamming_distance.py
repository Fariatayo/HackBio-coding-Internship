def hamming_distance(str1, str2):
    # Pad the shorter string with extra characters to match lengths
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len, '_')  # Pad with underscores
    str2 = str2.ljust(max_len, '_')  # Pad with underscores

    # Calculate the Hamming distance
    distance = sum(1 for a, b in zip(str1, str2) if a != b)
    return distance

# Your Slack username and Twitter handle
slack_username = "Fariat"
twitter_handle = "fariatxo"

# Calculate Hamming distance
distance = hamming_distance(slack_username, twitter_handle)
print(f"Hamming Distance: {distance}")
