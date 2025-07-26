import { useEffect, useRef } from 'react';

const ActivityClock = ({ hourlyActivity }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!hourlyActivity || hourlyActivity.length !== 24) return;

    const container = containerRef.current;
    container.innerHTML = '';

    const size = 300;
    const centerX = size / 2;
    const centerY = size / 2;
    const radius = 100;
    const maxActivity = Math.max(...hourlyActivity);

    // Create SVG
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', size);
    svg.setAttribute('height', size);
    svg.style.display = 'block';
    svg.style.margin = '0 auto';

    // Background circle
    const bgCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    bgCircle.setAttribute('cx', centerX);
    bgCircle.setAttribute('cy', centerY);
    bgCircle.setAttribute('r', radius + 20);
    bgCircle.setAttribute('fill', 'none');
    bgCircle.setAttribute('stroke', '#e5e7eb');
    bgCircle.setAttribute('stroke-width', '1');
    svg.appendChild(bgCircle);

    // Hour labels
    for (let hour = 0; hour < 24; hour++) {
      const angle = (hour * 15) - 90; // 15 degrees per hour, start at top
      const angleRad = (angle * Math.PI) / 180;
      const labelX = centerX + Math.cos(angleRad) * (radius + 35);
      const labelY = centerY + Math.sin(angleRad) * (radius + 35);

      const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', labelX);
      label.setAttribute('y', labelY);
      label.setAttribute('text-anchor', 'middle');
      label.setAttribute('dominant-baseline', 'middle');
      label.setAttribute('font-size', '12');
      label.setAttribute('fill', '#6b7280');
      label.setAttribute('font-weight', hour % 6 === 0 ? 'bold' : 'normal');
      label.textContent = hour === 0 ? '12AM' : hour === 12 ? '12PM' : hour > 12 ? `${hour - 12}PM` : `${hour}AM`;
      svg.appendChild(label);
    }

    // Activity bars
    for (let hour = 0; hour < 24; hour++) {
      const activity = hourlyActivity[hour];
      const angle = (hour * 15) - 90;
      const angleRad = (angle * Math.PI) / 180;

      // Calculate bar height based on activity
      const barHeight = maxActivity > 0 ? (activity / maxActivity) * 60 : 0;
      
      const startX = centerX + Math.cos(angleRad) * (radius - 20);
      const startY = centerY + Math.sin(angleRad) * (radius - 20);
      const endX = centerX + Math.cos(angleRad) * (radius - 20 + barHeight);
      const endY = centerY + Math.sin(angleRad) * (radius - 20 + barHeight);

      // Activity bar
      const bar = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      bar.setAttribute('x1', startX);
      bar.setAttribute('y1', startY);
      bar.setAttribute('x2', endX);
      bar.setAttribute('y2', endY);
      bar.setAttribute('stroke-width', '6');
      bar.setAttribute('stroke-linecap', 'round');
      bar.style.cursor = 'pointer';

      // Color based on activity level
      let color;
      if (activity === 0) {
        color = '#f3f4f6';
      } else {
        const intensity = activity / maxActivity;
        if (intensity <= 0.2) color = '#dbeafe';
        else if (intensity <= 0.4) color = '#93c5fd';
        else if (intensity <= 0.6) color = '#60a5fa';
        else if (intensity <= 0.8) color = '#3b82f6';
        else color = '#1d4ed8';
      }
      
      bar.setAttribute('stroke', color);

      // Tooltip on hover
      bar.addEventListener('mouseenter', () => {
        bar.setAttribute('stroke-width', '8');
        
        // Create tooltip
        const tooltip = document.createElement('div');
        tooltip.style.position = 'absolute';
        tooltip.style.background = '#1f2937';
        tooltip.style.color = 'white';
        tooltip.style.padding = '0.5rem';
        tooltip.style.borderRadius = '0.375rem';
        tooltip.style.fontSize = '0.875rem';
        tooltip.style.pointerEvents = 'none';
        tooltip.style.zIndex = '1000';
        tooltip.style.transform = 'translate(-50%, -100%)';
        tooltip.style.marginTop = '-0.5rem';
        tooltip.textContent = `${hour === 0 ? '12AM' : hour === 12 ? '12PM' : hour > 12 ? `${hour - 12}PM` : `${hour}AM`}: ${activity} videos`;
        
        const rect = container.getBoundingClientRect();
        tooltip.style.left = `${endX}px`;
        tooltip.style.top = `${endY}px`;
        
        container.style.position = 'relative';
        container.appendChild(tooltip);
        
        bar._tooltip = tooltip;
      });

      bar.addEventListener('mouseleave', () => {
        bar.setAttribute('stroke-width', '6');
        if (bar._tooltip) {
          container.removeChild(bar._tooltip);
          bar._tooltip = null;
        }
      });

      svg.appendChild(bar);
    }

    // Center circle with total
    const centerCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    centerCircle.setAttribute('cx', centerX);
    centerCircle.setAttribute('cy', centerY);
    centerCircle.setAttribute('r', '30');
    centerCircle.setAttribute('fill', '#f8fafc');
    centerCircle.setAttribute('stroke', '#e5e7eb');
    centerCircle.setAttribute('stroke-width', '2');
    svg.appendChild(centerCircle);

    const totalActivity = hourlyActivity.reduce((sum, count) => sum + count, 0);
    const centerText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    centerText.setAttribute('x', centerX);
    centerText.setAttribute('y', centerY - 5);
    centerText.setAttribute('text-anchor', 'middle');
    centerText.setAttribute('dominant-baseline', 'middle');
    centerText.setAttribute('font-size', '14');
    centerText.setAttribute('font-weight', 'bold');
    centerText.setAttribute('fill', '#1f2937');
    centerText.textContent = totalActivity;
    svg.appendChild(centerText);

    const centerLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    centerLabel.setAttribute('x', centerX);
    centerLabel.setAttribute('y', centerY + 10);
    centerLabel.setAttribute('text-anchor', 'middle');
    centerLabel.setAttribute('dominant-baseline', 'middle');
    centerLabel.setAttribute('font-size', '10');
    centerLabel.setAttribute('fill', '#6b7280');
    centerLabel.textContent = 'total';
    svg.appendChild(centerLabel);

    container.appendChild(svg);

  }, [hourlyActivity]);

  if (!hourlyActivity || hourlyActivity.length !== 24) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
        No hourly activity data available
      </div>
    );
  }

  return (
    <div>
      <div ref={containerRef} style={{ padding: '1rem' }} />
      <div style={{ textAlign: 'center', fontSize: '0.875rem', color: '#6b7280', marginTop: '0.5rem' }}>
        24-Hour Activity Pattern
      </div>
    </div>
  );
};

export default ActivityClock; 