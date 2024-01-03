#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/starships/9/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.name);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
