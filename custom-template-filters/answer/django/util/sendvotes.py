#!/usr/bin/env python3
#
# Script POSTs a bunch of random votes to polls in the Django Polls app.
# This is useful when you need to create a lot of vote data for testing.
#
# IMPORTANT:
# For this script to submit votes, you must disable CSRF preventtion.
# Edit mysite/settings.py and comment out one middleware line like this:
#
# MIDDLEWARE = [
#      ...,
#      # django.middleware.csrf.CsrfViewMiddleware',
#      ...
#      ]
#
# Script assumes the URL to post votes is http://localhost/polls/<n:int>/vote/
# as in the tutorial app.

from random import randint
import re, sys
import urllib, urllib.request, urllib.error

BASEURL = 'http://localhost:8000/polls/'
# url to get a poll and post a vite with placeholder for the poll number
GET_POLL = '{}/'
POST_VOTE = '{}/vote/'

def post_votes(poll_id, votes=1):
    """Post a fixed number of votes to each of the choices for a given poll.
       This provides some starting data for testing your polls application.

    Arguments:
        poll_id   is the numeric id of poll question to vote for.
        votes     is number of votes to cast for each choice.
    """
    choices = get_poll_choices(poll_id)
    nchoices = len(choices)
    print(f"Poll {poll_id} has {nchoices} choices. Sending {votes} votes.")
    vote_count = 0
    for choice in choices:
        post_vote(poll_id, choice, count=votes)
        vote_count += votes
    return vote_count

def post_random(poll_id, max_votes=3):
    """Post a random number of votes to each of the choices for a given poll.
       This provides some starting data for testing your polls application.

    Arguments:
        poll_id   is the numeric id of poll question to vote for.
        max_votes is max number of votes to cast for each choice.
    """
    choices = get_poll_choices(poll_id)
    nchoices = len(choices)
    print(f"Poll {poll_id} has {nchoices} choices. Sending random votes.")
    vote_count = 0
    for choice in choices:
        n = randint(0, max_votes)
        post_vote(poll_id, choice, count=n)
        vote_count += n
    return vote_count

def get_url(url:str):
    """Send GET request to a url and return the HTTP Response object"""
    try:
        request = urllib.request.Request(url,method='GET')
        response = urllib.request.urlopen(request)
        return response
    except (urllib.error.HTTPError, urllib.error.URLError) as ex:
        print("Exception getting url", url)
        print(str(ex))
        return None

def get_poll(poll_id):
    """Send GET request to a poll and return the HTTP Response object"""
    url = BASEURL + GET_POLL.format(poll_id)
    response = get_url(url)
    if not response:
        print("Could not get poll", poll_id)
    return response

def print_poll_headers(poll_id):
    """Print all the poll response headers.  For development use."""
    response = get_poll(poll_id)
    if not response: return
    headers = response.getheaders()
    for h in headers:
        print(f"{h}")

def get_poll_cookie(poll_id):
    """Get the poll cookie.  Use to get the CSRFTOKEN needed to submit POST."""
    response = get_poll(poll_id)
    if not response:
        return
    cookie = response.getheader('Set-Cookie')
    # Cookie we want is: 
    # csrftoken=ADFSADFASD123; expires=<date>; Max-Age=99999999; Path=/
    basecookie = cookie.split(';')[0]
    if basecookie.startswith("csrftoken"):
        return basecookie
    else:
        return ''

def get_poll_choices(poll_id):
    """Get all the ids of choices for a poll by parsing the poll body.
       Look for <input ... name="choice" value="xxx"> 
       where xxx is the choice id.
       Returns a list of choices. Returns empty list if poll is not found.
    """
    resp = get_poll(poll_id)
    choices = []
    if not resp: return choices  # no choices
    for rawline in resp:
        line = rawline.decode()
        match = re.match('.*name="choice".*value="(\d+)".*',line)
        if match:
            choices.append(match.group(1))
    resp.close()
    return choices

def post_vote(poll_id, choice, count=1):
    """Submit a vote to a particular choice (int) of poll_id.
       If count is given, post that many votes.
    """
    url = BASEURL + POST_VOTE.format(poll_id)
    # body of the request, form-encoded.
    # Template in tutorial submits 'choice=n'
    body = urllib.parse.urlencode( {"choice": choice} ).encode()
    #csrftoken = get_poll_cookie(poll_id)
    for n in range(count):
        try:
       	    request = urllib.request.Request(url,data=body,method='POST')
            #request.add_header('CSRF_TOKEN', csrftoken)
            response = urllib.request.urlopen(request)
            print(f"Poll {poll_id} sent vote for choice {choice}. ",
                  "Response code:", response.getcode())
        except (urllib.error.HTTPError, urllib.error.URLError) as ex:
            print("Exception during post to poll", poll_id)
            print(str(ex))
            return

def test_vote_for_poll(poll):
    choices = get_poll_choices(poll)
    # send 1 vote to each choice
    for choice in choices:
        post_vote(poll, choice)


if __name__ == '__main__':
    # send a get request to BASEURL to verify server is running
    response = get_url(BASEURL)
    if not response:
        print("No response from", BASEURL)
        print("Is the Django server running?")
        sys.exit(1)
    # You must use the poll question id numbers to submit votes
    for poll in [1,2,30,40]:
        # post up to 5 votes for each choice
        post_random( poll, 5)
