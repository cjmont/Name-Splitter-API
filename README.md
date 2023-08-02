# Name-Splitter-API

## Introduction

This repository contains a Flask-based API service that provides functionality to split full names into first name(s) and last name(s). The initial problem surfaced was that we had full names but for certain purposes, it was required to have first names and last names separately. The challenge was to do this for a dataset with potentially very diverse name structures.

## Solution

The solution implemented here uses Python's NLTK library's names corpus to determine if a part of the full name is a well-known name. If it is, it's classified as a first name. Otherwise, it's considered a last name. The API then returns the first name and the last name as two separate strings.

However, please note that this solution is primarily geared towards English names, as the NLTK corpus is primarily based on English names. If working with names in other languages, a different approach or a list of names in the desired language might be needed.

## Usage

To use this API, you need to make a POST request to the '/split_name' route with a JSON body containing the full name you want to split, formatted as: `{'fullname': 'Your Full Name'}`. The API will return a JSON object with the first name and last name split.

For example:

```json
Request:
POST /split_name
Content-Type: application/json
{
    "fullname": "Carlos Rivera M"
}

Response:
{
    "firstname": "Carlos",
    "lastname": "Rivera M"
}
