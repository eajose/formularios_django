# Use an official node runtime as a parent image
FROM node:10

WORKDIR /app

# Install dependencies
# COPY package.json yarn.lock /app/
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

RUN npm install

# Add rest of the client code
COPY . /app

EXPOSE 3000

# CMD npm start