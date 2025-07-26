import { useEffect, useRef } from 'react';

const WeeklyPattern = ({ weeklyActivity }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!weeklyActivity || weeklyActivity.length !== 7) return;

    const container = containerRef.current;
    container.innerHTML = '';

    const width = 400;
    const height = 250;
    const margin = { top: 20, right: 20, bottom: 40, left: 40 };
    const chartWidth = width - margin.left - margin.right;
    const chartHeight = height - margin.top - margin.bottom;

    const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const maxActivity = Math.max(...weeklyActivity);

    // Create SVG
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', width);
    svg.setAttribute('height', height);
    svg.style.display = 'block';
    svg.style.margin = '0 auto';

    // Background
    const bg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    bg.setAttribute('x', margin.left);
    bg.setAttribute('y', margin.top);
    bg.setAttribute('width', chartWidth);
    bg.setAttribute('height', chartHeight);
    bg.setAttribute('fill', '#fafafa');
    bg.setAttribute('stroke', '#e5e7eb');
    svg.appendChild(bg);

    // Grid lines
    for (let i = 0; i <= 5; i++) {
      const y = margin.top + (chartHeight / 5) * i;
      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', margin.left);
      line.setAttribute('x2', margin.left + chartWidth);
      line.setAttribute('y1', y);
      line.setAttribute('y2', y);
      line.setAttribute('stroke', '#e5e7eb');
      line.setAttribute('stroke-width', '1');
      svg.appendChild(line);

      // Y-axis labels
      const value = Math.round((maxActivity / 5) * (5 - i));
      const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', margin.left - 10);
      label.setAttribute('y', y);
      label.setAttribute('text-anchor', 'end');
      label.setAttribute('dominant-baseline', 'middle');
      label.setAttribute('font-size', '10');
      label.setAttribute('fill', '#6b7280');
      label.textContent = value;
      svg.appendChild(label);
    }

    // Bars
    const barWidth = chartWidth / 7 - 10;
    weeklyActivity.forEach((activity, i) => {
      const x = margin.left + i * (chartWidth / 7) + 5;
      const barHeight = maxActivity > 0 ? (activity / maxActivity) * chartHeight : 0;
      const y = margin.top + chartHeight - barHeight;

      // Bar background
      const bgBar = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      bgBar.setAttribute('x', x);
      bgBar.setAttribute('y', margin.top);
      bgBar.setAttribute('width', barWidth);
      bgBar.setAttribute('height', chartHeight);
      bgBar.setAttribute('fill', '#f3f4f6');
      bgBar.setAttribute('stroke', '#e5e7eb');
      bgBar.setAttribute('stroke-width', '1');
      svg.appendChild(bgBar);

      // Animated bar
      const bar = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      bar.setAttribute('x', x);
      bar.setAttribute('y', margin.top + chartHeight);
      bar.setAttribute('width', barWidth);
      bar.setAttribute('height', 0);
      bar.setAttribute('rx', '3');
      bar.style.cursor = 'pointer';

      // Color based on day type and activity
      let color;
      if (i === 0 || i === 6) { // Weekend
        color = activity > 0 ? '#ec4899' : '#f3e8ff';
      } else { // Weekday
        color = activity > 0 ? '#3b82f6' : '#dbeafe';
      }
      bar.setAttribute('fill', color);

      // Animate bar
      setTimeout(() => {
        bar.setAttribute('y', y);
        bar.setAttribute('height', barHeight);
        bar.style.transition = 'all 0.8s ease-out';
      }, i * 100);

      // Hover effects
      bar.addEventListener('mouseenter', () => {
        bar.setAttribute('opacity', '0.8');
        
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
        tooltip.innerHTML = `
          <div style="font-weight: bold;">${dayNames[i]}</div>
          <div>${activity} videos watched</div>
        `;
        
        tooltip.style.left = `${x + barWidth / 2}px`;
        tooltip.style.top = `${y}px`;
        
        container.style.position = 'relative';
        container.appendChild(tooltip);
        
        bar._tooltip = tooltip;
      });

      bar.addEventListener('mouseleave', () => {
        bar.setAttribute('opacity', '1');
        if (bar._tooltip) {
          container.removeChild(bar._tooltip);
          bar._tooltip = null;
        }
      });

      svg.appendChild(bar);

      // Day labels
      const dayLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      dayLabel.setAttribute('x', x + barWidth / 2);
      dayLabel.setAttribute('y', height - 5);
      dayLabel.setAttribute('text-anchor', 'middle');
      dayLabel.setAttribute('font-size', '10');
      dayLabel.setAttribute('fill', '#6b7280');
      dayLabel.setAttribute('font-weight', (i === 0 || i === 6) ? 'bold' : 'normal');
      dayLabel.textContent = dayNames[i].substring(0, 3);
      svg.appendChild(dayLabel);

      // Activity value on top of bar
      if (activity > 0) {
        const valueLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        valueLabel.setAttribute('x', x + barWidth / 2);
        valueLabel.setAttribute('y', y - 5);
        valueLabel.setAttribute('text-anchor', 'middle');
        valueLabel.setAttribute('font-size', '11');
        valueLabel.setAttribute('font-weight', 'bold');
        valueLabel.setAttribute('fill', color);
        valueLabel.textContent = activity;
        
        // Animate label appearance
        valueLabel.setAttribute('opacity', '0');
        setTimeout(() => {
          valueLabel.setAttribute('opacity', '1');
          valueLabel.style.transition = 'opacity 0.5s ease-out';
        }, i * 100 + 400);
        
        svg.appendChild(valueLabel);
      }
    });

    // Legend
    const legend = document.createElement('div');
    legend.style.display = 'flex';
    legend.style.justifyContent = 'center';
    legend.style.gap = '1.5rem';
    legend.style.marginTop = '1rem';
    legend.style.fontSize = '0.875rem';

    const weekdayItem = document.createElement('div');
    weekdayItem.style.display = 'flex';
    weekdayItem.style.alignItems = 'center';
    weekdayItem.style.gap = '0.5rem';

    const weekdayDot = document.createElement('div');
    weekdayDot.style.width = '12px';
    weekdayDot.style.height = '12px';
    weekdayDot.style.backgroundColor = '#3b82f6';
    weekdayDot.style.borderRadius = '2px';

    const weekdayLabel = document.createElement('span');
    weekdayLabel.textContent = 'Weekdays';
    weekdayLabel.style.color = '#374151';

    weekdayItem.appendChild(weekdayDot);
    weekdayItem.appendChild(weekdayLabel);

    const weekendItem = document.createElement('div');
    weekendItem.style.display = 'flex';
    weekendItem.style.alignItems = 'center';
    weekendItem.style.gap = '0.5rem';

    const weekendDot = document.createElement('div');
    weekendDot.style.width = '12px';
    weekendDot.style.height = '12px';
    weekendDot.style.backgroundColor = '#ec4899';
    weekendDot.style.borderRadius = '2px';

    const weekendLabel = document.createElement('span');
    weekendLabel.textContent = 'Weekends';
    weekendLabel.style.color = '#374151';

    weekendItem.appendChild(weekendDot);
    weekendItem.appendChild(weekendLabel);

    legend.appendChild(weekdayItem);
    legend.appendChild(weekendItem);

    container.appendChild(svg);
    container.appendChild(legend);

  }, [weeklyActivity]);

  if (!weeklyActivity || weeklyActivity.length !== 7) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
        No weekly activity data available
      </div>
    );
  }

  return (
    <div>
      <div ref={containerRef} style={{ padding: '1rem' }} />
    </div>
  );
};

export default WeeklyPattern; 