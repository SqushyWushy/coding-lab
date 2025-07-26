#!/bin/bash

echo "🌐 COMPLETE LOCAL SITE TESTING"
echo "==============================="
echo

# Function to check if a port is in use
check_port() {
    lsof -i :$1 >/dev/null 2>&1
}

# Function to wait for a service to be ready
wait_for_service() {
    local url=$1
    local name=$2
    local max_attempts=30
    local attempt=1
    
    echo "⏳ Waiting for $name to start..."
    while [ $attempt -le $max_attempts ]; do
        if curl -s "$url" >/dev/null 2>&1; then
            echo "✅ $name is ready!"
            return 0
        fi
        echo "   Attempt $attempt/$max_attempts..."
        sleep 2
        attempt=$((attempt + 1))
    done
    
    echo "❌ $name failed to start after $max_attempts attempts"
    return 1
}

echo "📋 STEP 1: Check Backend Status"
echo "================================"

if check_port 4000; then
    echo "✅ Backend is already running on port 4000"
    if curl -s http://localhost:4000/ >/dev/null 2>&1; then
        echo "✅ Backend is responding"
    else
        echo "⚠️  Backend port is occupied but not responding"
    fi
else
    echo "🚀 Starting backend server..."
    cd exposed/backend
    npm start > backend.log 2>&1 &
    BACKEND_PID=$!
    echo "   Backend PID: $BACKEND_PID"
    
    if wait_for_service "http://localhost:4000" "Backend"; then
        echo "✅ Backend started successfully"
    else
        echo "❌ Backend failed to start"
        echo "Backend logs:"
        tail -20 backend.log 2>/dev/null || echo "No backend logs found"
        exit 1
    fi
    cd ../..
fi

echo
echo "📋 STEP 2: Check Frontend Status"
echo "================================="

if check_port 3000; then
    echo "✅ Frontend is already running on port 3000"
else
    echo "🚀 Starting frontend server..."
    cd exposed/frontend
    
    # Check if node_modules exists
    if [ ! -d "node_modules" ]; then
        echo "📦 Installing frontend dependencies..."
        npm install
    fi
    
    npm start > frontend.log 2>&1 &
    FRONTEND_PID=$!
    echo "   Frontend PID: $FRONTEND_PID"
    
    if wait_for_service "http://localhost:3000" "Frontend"; then
        echo "✅ Frontend started successfully"
    else
        echo "❌ Frontend failed to start"
        echo "Frontend logs:"
        tail -20 frontend.log 2>/dev/null || echo "No frontend logs found"
        exit 1
    fi
    cd ../..
fi

echo
echo "📋 STEP 3: Test Backend API"
echo "==========================="

echo "🧪 Testing TikTok file processing..."

# Test with the originally problematic file
response=$(curl -X POST http://localhost:4000/api/analyze \
    -F "tiktokData=@exposed/backend/example-data/user_data_tiktok 3.json" \
    -s | jq -r '.success // "error"' 2>/dev/null)

if [ "$response" = "true" ]; then
    echo "✅ TikTok analysis API working perfectly!"
    
    # Get some stats
    videos=$(curl -X POST http://localhost:4000/api/analyze \
        -F "tiktokData=@exposed/backend/example-data/user_data_tiktok 3.json" \
        -s | jq -r '.data.summary.totalVideosWatched // 0' 2>/dev/null)
    
    echo "📊 Successfully processed $videos videos"
else
    echo "❌ TikTok analysis API failed"
    echo "Response: $response"
fi

echo
echo "🎯 TESTING INSTRUCTIONS"
echo "======================="
echo
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://localhost:4000"
echo
echo "📂 Test Files Available:"
echo "   • exposed/backend/example-data/user_data_tiktok.json (OLD format)"
echo "   • exposed/backend/example-data/user_data_tiktok 2.json (NEW format)"
echo "   • exposed/backend/example-data/user_data_tiktok 3.json (Originally problematic)"
echo
echo "✅ MANUAL TESTING CHECKLIST:"
echo "=============================="
echo "□ 1. Open http://localhost:3000 in your browser"
echo "□ 2. Upload user_data_tiktok.json (should show ~26K videos)"
echo "□ 3. Upload user_data_tiktok 2.json (should show ~16K videos)"  
echo "□ 4. Upload user_data_tiktok 3.json (should show ~125K videos - this was broken before!)"
echo "□ 5. Verify all analyses complete without 'pattern matching' errors"
echo "□ 6. Check that AI summaries are generated"
echo "□ 7. Verify data visualizations appear correctly"
echo
echo "🔍 WHAT TO LOOK FOR:"
echo "===================="
echo "✅ No upload errors"
echo "✅ Analysis completes for all file formats"
echo "✅ Video counts match expected numbers"
echo "✅ AI personality analysis appears"
echo "✅ No console errors in browser"
echo
echo "🛑 TO STOP SERVERS:"
echo "==================="
echo "   Backend:  pkill -f 'node.*app.js'"
echo "   Frontend: pkill -f 'react-scripts'"
echo "   Both:     ./stop_servers.sh"
echo
echo "🎉 Ready for testing! Open http://localhost:3000 and upload TikTok files!" 