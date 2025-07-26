#!/bin/bash

echo "🚀 QUICK START - Complete Site Testing"
echo "======================================"
echo

# Check current directory
if [[ ! $(pwd) == *"exposed"* ]]; then
    echo "📂 Moving to exposed directory..."
    cd exposed 2>/dev/null || {
        echo "❌ Please run this from the datahackfest25 directory"
        exit 1
    }
fi

echo "🔧 Starting Backend Server..."
echo "=============================="
cd backend
npm start > backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend starting with PID: $BACKEND_PID"

echo
echo "⏳ Waiting for backend to be ready..."
for i in {1..15}; do
    if curl -s http://localhost:4000/ >/dev/null 2>&1; then
        echo "✅ Backend is ready on http://localhost:4000"
        break
    fi
    echo "   Waiting... ($i/15)"
    sleep 2
    if [ $i -eq 15 ]; then
        echo "❌ Backend failed to start. Check backend.log"
        exit 1
    fi
done

echo
echo "🎨 Starting Frontend Server..."
echo "==============================="
cd ../frontend

# Check if dependencies are installed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

npm start > frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend starting with PID: $FRONTEND_PID"

echo
echo "⏳ Waiting for frontend to be ready..."
for i in {1..30}; do
    if curl -s http://localhost:3000/ >/dev/null 2>&1; then
        echo "✅ Frontend is ready on http://localhost:3000"
        break
    fi
    echo "   Waiting... ($i/30)"
    sleep 2
    if [ $i -eq 30 ]; then
        echo "❌ Frontend failed to start. Check frontend.log"
        exit 1
    fi
done

echo
echo "🎉 BOTH SERVICES ARE RUNNING!"
echo "=============================="
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://localhost:4000"
echo
echo "📂 Test Files Ready:"
echo "   • backend/example-data/user_data_tiktok.json (OLD format)"
echo "   • backend/example-data/user_data_tiktok 2.json (NEW format)"
echo "   • backend/example-data/user_data_tiktok 3.json (FIXED - was broken!)"
echo
echo "✅ READY FOR TESTING!"
echo "===================="
echo "1. Open http://localhost:3000 in your browser"
echo "2. Upload the TikTok files above"
echo "3. Verify all process without 'pattern matching' errors"
echo "4. Check that ~125K videos process from file 3 (previously broken)"
echo
echo "🛑 To stop both servers: ./stop_servers.sh"
echo
echo "🎯 Opening browser in 3 seconds..."
sleep 3

# Try to open browser (works on macOS)
if command -v open >/dev/null 2>&1; then
    open http://localhost:3000
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open http://localhost:3000
else
    echo "Please open http://localhost:3000 manually"
fi

echo
echo "✨ Happy testing! The TikTok analysis should work perfectly now!" 