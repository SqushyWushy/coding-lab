#!/bin/bash

echo "🧪 TESTING ALL TIKTOK FILES YOURSELF"
echo "======================================"
echo

# Check if server is running
echo "🔍 Checking if server is running..."
if curl -s http://localhost:4000/ > /dev/null 2>&1; then
    echo "✅ Server is running on http://localhost:4000"
else
    echo "❌ Server is not running. Please run 'npm start' first."
    exit 1
fi

echo
echo "📂 Testing all TikTok files..."
echo

# Test File 1: Old Format
echo "1️⃣  Testing user_data_tiktok.json (OLD FORMAT)"
echo "   File: example-data/user_data_tiktok.json"
response1=$(curl -X POST http://localhost:4000/api/analyze \
    -F "tiktokData=@example-data/user_data_tiktok.json" \
    -s | jq -r '.success // "error"')
if [ "$response1" = "true" ]; then
    echo "   ✅ SUCCESS - Old format works!"
    # Get video count
    videos1=$(curl -X POST http://localhost:4000/api/analyze \
        -F "tiktokData=@example-data/user_data_tiktok.json" \
        -s | jq -r '.data.summary.totalVideosWatched // 0')
    echo "   📊 Videos processed: $videos1"
else
    echo "   ❌ FAILED - Error processing old format"
fi

echo

# Test File 2: New Format
echo "2️⃣  Testing user_data_tiktok 2.json (NEW FORMAT)"
echo "   File: example-data/user_data_tiktok 2.json"
response2=$(curl -X POST http://localhost:4000/api/analyze \
    -F "tiktokData=@example-data/user_data_tiktok 2.json" \
    -s | jq -r '.success // "error"')
if [ "$response2" = "true" ]; then
    echo "   ✅ SUCCESS - New format works!"
    videos2=$(curl -X POST http://localhost:4000/api/analyze \
        -F "tiktokData=@example-data/user_data_tiktok 2.json" \
        -s | jq -r '.data.summary.totalVideosWatched // 0')
    echo "   📊 Videos processed: $videos2"
else
    echo "   ❌ FAILED - Error processing new format"
fi

echo

# Test File 3: Originally Problematic
echo "3️⃣  Testing user_data_tiktok 3.json (ORIGINALLY PROBLEMATIC)"
echo "   File: example-data/user_data_tiktok 3.json"
response3=$(curl -X POST http://localhost:4000/api/analyze \
    -F "tiktokData=@example-data/user_data_tiktok 3.json" \
    -s | jq -r '.success // "error"')
if [ "$response3" = "true" ]; then
    echo "   ✅ SUCCESS - Previously broken file now works!"
    videos3=$(curl -X POST http://localhost:4000/api/analyze \
        -F "tiktokData=@example-data/user_data_tiktok 3.json" \
        -s | jq -r '.data.summary.totalVideosWatched // 0')
    echo "   📊 Videos processed: $videos3"
else
    echo "   ❌ FAILED - Still having issues"
fi

echo

# Test File 4: Copy without spaces
echo "4️⃣  Testing user_data_tiktok_3.json (COPY WITHOUT SPACES)"
echo "   File: example-data/user_data_tiktok_3.json"
response4=$(curl -X POST http://localhost:4000/api/analyze \
    -F "tiktokData=@example-data/user_data_tiktok_3.json" \
    -s | jq -r '.success // "error"')
if [ "$response4" = "true" ]; then
    echo "   ✅ SUCCESS - Copy works perfectly!"
    videos4=$(curl -X POST http://localhost:4000/api/analyze \
        -F "tiktokData=@example-data/user_data_tiktok_3.json" \
        -s | jq -r '.data.summary.totalVideosWatched // 0')
    echo "   📊 Videos processed: $videos4"
else
    echo "   ❌ FAILED - Copy has issues"
fi

echo
echo "🏆 FINAL RESULTS"
echo "================"

# Count successes
success_count=0
if [ "$response1" = "true" ]; then ((success_count++)); fi
if [ "$response2" = "true" ]; then ((success_count++)); fi
if [ "$response3" = "true" ]; then ((success_count++)); fi
if [ "$response4" = "true" ]; then ((success_count++)); fi

echo "📊 Files working: $success_count/4"

if [ $success_count -eq 4 ]; then
    echo "🎉 ALL TIKTOK FILES WORK PERFECTLY!"
    echo "✅ Pattern matching error is completely resolved"
    echo "✅ Both old and new formats are supported"
else
    echo "⚠️  Some files still have issues"
fi

echo
echo "💡 TIP: You can also test individual files with:"
echo "   curl -X POST http://localhost:4000/api/analyze -F 'tiktokData=@example-data/FILENAME.json'" 