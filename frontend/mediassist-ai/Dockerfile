FROM node:18

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy rest of frontend code
COPY . .

# Expose Vite port
EXPOSE 5173

# Run Vite
CMD ["npm", "run", "dev", "--", "--host"]