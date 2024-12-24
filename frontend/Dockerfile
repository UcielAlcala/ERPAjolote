# frontend/Dockerfile.dev

FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install -g npm@latest
RUN npm install

COPY . .

EXPOSE 4200
CMD ["npm", "start"]
