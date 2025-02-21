# Use Node.js as the base image
FROM node:20-slim AS build

# Install the latest version of corepack
RUN npm install -g corepack@latest

# Enable pnpm
RUN corepack enable

# Set the working directory inside the nested project folder
WORKDIR /app

# Copy package.json and pnpm-lock.yaml
COPY package.json pnpm-lock.yaml ./

# Install dependencies using pnpm
RUN pnpm install

# Copy the entire frontend project
COPY . .

# Build the frontend application
RUN pnpm run build

# Use Nginx for serving the built frontend
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the port for Nginx
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
