#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
	const data = JSON.parse(body);
	const uniqueUserIds = new Set();
	data.forEach(entry => {
		uniqueUserIds.add(entry.userId);
	});
	const numUniqueUserIds = uniqueUserIds.size;
	console.log("Number of unique userIds:", numUniqueUserIds);
});
