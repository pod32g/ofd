FROM node:14.15.3-slim

RUN mkdir /code

ADD . /code

WORKDIR /code

RUN yarn
RUN yarn build
RUN mkdir /serve

RUN mv ./public /serve

WORKDIR /serve
RUN rm -rf /code


RUN yarn global add serve

EXPOSE 5000
CMD ["serve", "-s", "public"]
