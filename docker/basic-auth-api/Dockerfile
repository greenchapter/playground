FROM node:lts-alpine
WORKDIR /usr/src/app
COPY . .
RUN npm install
EXPOSE 80
ENTRYPOINT ["node"]
CMD ["server.js"]
