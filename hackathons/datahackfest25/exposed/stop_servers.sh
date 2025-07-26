#!/bin/bash

echo "🛑 Stopping local development servers..."

# Stop backend
echo "Stopping backend server..."
pkill -f "node.*app.js"

# Stop frontend  
echo "Stopping frontend server..."
pkill -f "react-scripts"

# Stop any npm processes
pkill -f "npm.*start"

echo "✅ All servers stopped!"

# Check if ports are free
sleep 2
if ! lsof -i :4000 >/dev/null 2>&1; then
    echo "✅ Port 4000 (backend) is free"
else
    echo "⚠️  Port 4000 still in use"
fi

if ! lsof -i :3000 >/dev/null 2>&1; then
    echo "✅ Port 3000 (frontend) is free"
else
    echo "⚠️  Port 3000 still in use"
fi 