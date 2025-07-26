import { useEffect, useRef } from 'react';

const WordCloud = ({ words, title = "Word Cloud" }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!words || Object.keys(words).length === 0) return;

    const container = containerRef.current;
    container.innerHTML = '';

    const width = 500;
    const height = 300;

    // Convert words object to array and sort by frequency
    const wordArray = Object.entries(words)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 50); // Limit to top 50 words

    if (wordArray.length === 0) return;

    const maxCount = Math.max(...wordArray.map(([_, count]) => count));
    const minCount = Math.min(...wordArray.map(([_, count]) => count));

    // Create container div
    const cloudContainer = document.createElement('div');
    cloudContainer.style.width = `${width}px`;
    cloudContainer.style.height = `${height}px`;
    cloudContainer.style.position = 'relative';
    cloudContainer.style.margin = '0 auto';
    cloudContainer.style.border = '1px solid #e5e7eb';
    cloudContainer.style.borderRadius = '0.75rem';
    cloudContainer.style.backgroundColor = '#fafafa';
    cloudContainer.style.overflow = 'hidden';

    // Color palette
    const colors = [
      '#3b82f6', '#ef4444', '#10b981', '#f59e0b', 
      '#8b5cf6', '#ec4899', '#06b6d4', '#84cc16'
    ];

    // Calculate positions and sizes
    const placedWords = [];
    
    wordArray.forEach(([word, count], index) => {
      // Calculate font size based on frequency
      const normalizedCount = (count - minCount) / (maxCount - minCount);
      const fontSize = Math.max(12, Math.min(36, 12 + normalizedCount * 24));
      
      // Color based on frequency
      const colorIndex = Math.floor((normalizedCount * colors.length));
      const color = colors[Math.min(colorIndex, colors.length - 1)];

      // Create word element
      const wordElement = document.createElement('span');
      wordElement.textContent = word;
      wordElement.style.position = 'absolute';
      wordElement.style.fontSize = `${fontSize}px`;
      wordElement.style.fontWeight = normalizedCount > 0.7 ? 'bold' : normalizedCount > 0.4 ? '600' : '400';
      wordElement.style.color = color;
      wordElement.style.cursor = 'pointer';
      wordElement.style.transition = 'all 0.2s ease';
      wordElement.style.userSelect = 'none';
      wordElement.style.whiteSpace = 'nowrap';

      // Simple positioning algorithm (spiral-like)
      let positioned = false;
      let attempts = 0;
      const maxAttempts = 100;

      while (!positioned && attempts < maxAttempts) {
        let x, y;
        
        if (attempts < 10) {
          // Try center positions first
          const angle = (attempts * 137.5) * (Math.PI / 180); // Golden angle
          const radius = attempts * 15;
          x = width / 2 + Math.cos(angle) * radius;
          y = height / 2 + Math.sin(angle) * radius;
        } else {
          // Random positioning
          x = Math.random() * (width - fontSize * word.length * 0.6);
          y = Math.random() * (height - fontSize);
        }

        // Check bounds
        const wordWidth = fontSize * word.length * 0.6;
        const wordHeight = fontSize;
        
        if (x >= 0 && y >= 0 && 
            x + wordWidth <= width && 
            y + wordHeight <= height) {
          
          // Check collision with existing words
          let collision = false;
          for (const placed of placedWords) {
            if (!(x + wordWidth < placed.x || 
                  x > placed.x + placed.width || 
                  y + wordHeight < placed.y || 
                  y > placed.y + placed.height)) {
              collision = true;
              break;
            }
          }

          if (!collision) {
            positioned = true;
            placedWords.push({
              x: x,
              y: y,
              width: wordWidth,
              height: wordHeight
            });

            wordElement.style.left = `${x}px`;
            wordElement.style.top = `${y}px`;
          }
        }
        
        attempts++;
      }

      // If couldn't position properly, use a fallback position
      if (!positioned) {
        const fallbackX = (index % 10) * (width / 10);
        const fallbackY = Math.floor(index / 10) * 30 + 20;
        wordElement.style.left = `${fallbackX}px`;
        wordElement.style.top = `${fallbackY}px`;
      }

      // Add hover effects
      wordElement.addEventListener('mouseenter', () => {
        wordElement.style.transform = 'scale(1.2)';
        wordElement.style.zIndex = '10';
        wordElement.style.fontWeight = 'bold';
        
        // Create tooltip
        const tooltip = document.createElement('div');
        tooltip.style.position = 'absolute';
        tooltip.style.background = '#1f2937';
        tooltip.style.color = 'white';
        tooltip.style.padding = '0.5rem';
        tooltip.style.borderRadius = '0.375rem';
        tooltip.style.fontSize = '0.875rem';
        tooltip.style.pointerEvents = 'none';
        tooltip.style.zIndex = '20';
        tooltip.style.transform = 'translate(-50%, -100%)';
        tooltip.style.marginTop = '-0.5rem';
        tooltip.textContent = `"${word}": used ${count} times`;
        
        const rect = wordElement.getBoundingClientRect();
        const containerRect = cloudContainer.getBoundingClientRect();
        tooltip.style.left = `${rect.left - containerRect.left + rect.width / 2}px`;
        tooltip.style.top = `${rect.top - containerRect.top}px`;
        
        cloudContainer.appendChild(tooltip);
        wordElement._tooltip = tooltip;
      });

      wordElement.addEventListener('mouseleave', () => {
        wordElement.style.transform = 'scale(1)';
        wordElement.style.zIndex = 'auto';
        wordElement.style.fontWeight = normalizedCount > 0.7 ? 'bold' : normalizedCount > 0.4 ? '600' : '400';
        
        if (wordElement._tooltip) {
          cloudContainer.removeChild(wordElement._tooltip);
          wordElement._tooltip = null;
        }
      });

      // Add click effect
      wordElement.addEventListener('click', () => {
        wordElement.style.animation = 'pulse 0.3s ease-in-out';
        setTimeout(() => {
          wordElement.style.animation = '';
        }, 300);
      });

      cloudContainer.appendChild(wordElement);
    });

    container.appendChild(cloudContainer);

    // Add pulse animation
    const style = document.createElement('style');
    style.textContent = `
      @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
      }
    `;
    document.head.appendChild(style);

  }, [words]);

  if (!words || Object.keys(words).length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
        No word data available
      </div>
    );
  }

  return (
    <div>
      <div ref={containerRef} style={{ padding: '1rem' }} />
      <div style={{ textAlign: 'center', fontSize: '0.875rem', color: '#6b7280', marginTop: '0.5rem' }}>
        {title} - Hover over words to see frequency
      </div>
    </div>
  );
};

export default WordCloud; 