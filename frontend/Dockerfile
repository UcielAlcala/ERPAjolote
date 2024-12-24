# frontend/Dockerfile.dev

FROM node:20-alpine

WORKDIR /app



COPY package.json package-lock.json ./
# Instala Angular CLI globalmente
RUN npm install -g @angular/cli & npm install --include=dev

COPY . .


EXPOSE 4200
CMD ["npm", "start"]
