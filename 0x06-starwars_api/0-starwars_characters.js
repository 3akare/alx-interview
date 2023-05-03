#!/usr/bin/node
const request = require('request');

const getCharacter = async () => {
  const MovieId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${MovieId}`;
  request(url, async (err, res, body) => {
    if (err) console.log(err);
    else {
      const data = JSON.parse(body);
      try {
        for (const element of data.characters) {
          (
            await new Promise((resolve, reject) => {
              request(element, (err, res, body) => {
                if (err) reject(err);
                else {
                  JSON.parse(body).name ? console.log(JSON.parse(body).name) : console.log(err);
                  resolve();
                }
              });
            }
            )
          );
        }
      } catch (err) {
        console.log(res.statusCode);
      }
    }
  });
};

getCharacter();
