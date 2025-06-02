FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn --frozen-lockfile

COPY . .

RUN yarn build

FROM nginx:alpine
LABEL authors="mvmarinov@pm.me"

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf.template /etc/nginx/templates/default.conf.template

ENV MAX_BODY_SIZE="5m"
