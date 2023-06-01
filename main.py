import tkinter as tk
from tkinter import messagebox
import tweepy

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Function to post tweet
def post_tweet():
    tweet = tweet_entry.get()
    if tweet:
        try:
            api.update_status(tweet)
            messagebox.showinfo("Success", "Tweet posted successfully!")
            tweet_entry.delete(0, tk.END)
        except tweepy.TweepError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "Please enter a tweet!")

# Create GUI window
window = tk.Tk()
window.title("TBP")
window.geometry("400x200")

# Create tweet entry field
tweet_label = tk.Label(window, text="Tweet:")
tweet_label.pack()
tweet_entry = tk.Entry(window, width=40)
tweet_entry.pack()

# Create post tweet button
post_button = tk.Button(window, text="Post Tweet", command=post_tweet)
post_button.pack()

# Run the GUI event loop
window.mainloop()
