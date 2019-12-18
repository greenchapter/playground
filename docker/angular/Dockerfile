FROM node:latest as builder
COPY . ./tmp
WORKDIR /tmp
RUN npm ci && npm run ng build -- --prod --output-path=dist

FROM nginx:alpine
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /tmp/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
