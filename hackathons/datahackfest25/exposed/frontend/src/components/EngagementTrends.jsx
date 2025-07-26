import { useEffect, useRef } from 'react';

const EngagementTrends = ({ engagementTrends }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!engagementTrends || Object.keys(engagementTrends).length === 0) return;

    const container = containerRef.current;
    container.innerHTML = '';

    const width = 600;
    const height = 300;
    const margin = { top: 20, right: 80, bottom: 40, left: 60 };
    const chartWidth = width - margin.left - margin.right;
    const chartHeight = height - margin.top - margin.bottom;

    // Prepare data
    const months = Object.keys(engagementTrends).sort();
    const data = months.map(month => ({
      month,
      ...engagementTrends[month]
    }));

    // Get max values for scaling
    const maxVideos = Math.max(...data.map(d => d.videos || 0));
    const maxLikes = Math.max(...data.map(d => d.likes || 0));
    const maxComments = Math.max(...data.map(d => d.comments || 0));
    const maxSearches = Math.max(...data.map(d => d.searches || 0));
    const globalMax = Math.max(maxVideos, maxLikes, maxComments, maxSearches);

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
      const value = Math.round((globalMax / 5) * (5 - i));
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

    // X-axis labels
    data.forEach((d, i) => {
      const x = margin.left + (chartWidth / (data.length - 1)) * i;
      const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', x);
      label.setAttribute('y', height - 10);
      label.setAttribute('text-anchor', 'middle');
      label.setAttribute('font-size', '10');
      label.setAttribute('fill', '#6b7280');
      const date = new Date(d.month + '-01');
      label.textContent = date.toLocaleDateString('en-US', { month: 'short', year: '2-digit' });
      svg.appendChild(label);
    });

    // Create lines for each metric
    const metrics = [
      { key: 'videos', color: '#3b82f6', label: 'Videos' },
      { key: 'likes', color: '#ef4444', label: 'Likes' },
      { key: 'comments', color: '#10b981', label: 'Comments' },
      { key: 'searches', color: '#f59e0b', label: 'Searches' }
    ];

    metrics.forEach(metric => {
      if (!data.some(d => d[metric.key] > 0)) return; // Skip if no data

      // Create path
      let pathData = '';
      data.forEach((d, i) => {
        const x = margin.left + (chartWidth / (data.length - 1)) * i;
        const value = d[metric.key] || 0;
        const y = margin.top + chartHeight - (value / globalMax) * chartHeight;
        
        if (i === 0) {
          pathData += `M ${x} ${y}`;
        } else {
          pathData += ` L ${x} ${y}`;
        }
      });

      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', pathData);
      path.setAttribute('stroke', metric.color);
      path.setAttribute('stroke-width', '3');
      path.setAttribute('fill', 'none');
      path.setAttribute('stroke-linecap', 'round');
      path.setAttribute('stroke-linejoin', 'round');
      svg.appendChild(path);

      // Add data points
      data.forEach((d, i) => {
        const x = margin.left + (chartWidth / (data.length - 1)) * i;
        const value = d[metric.key] || 0;
        const y = margin.top + chartHeight - (value / globalMax) * chartHeight;

        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', x);
        circle.setAttribute('cy', y);
        circle.setAttribute('r', '4');
        circle.setAttribute('fill', metric.color);
        circle.setAttribute('stroke', 'white');
        circle.setAttribute('stroke-width', '2');
        circle.style.cursor = 'pointer';

        // Tooltip
        circle.addEventListener('mouseenter', () => {
          circle.setAttribute('r', '6');
          
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
          
          const date = new Date(d.month + '-01');
          tooltip.innerHTML = `
            <div style="font-weight: bold; margin-bottom: 0.25rem;">
              ${date.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}
            </div>
            <div style="color: ${metric.color};">
              ${metric.label}: ${value}
            </div>
          `;
          
          tooltip.style.left = `${x}px`;
          tooltip.style.top = `${y}px`;
          
          container.style.position = 'relative';
          container.appendChild(tooltip);
          
          circle._tooltip = tooltip;
        });

        circle.addEventListener('mouseleave', () => {
          circle.setAttribute('r', '4');
          if (circle._tooltip) {
            container.removeChild(circle._tooltip);
            circle._tooltip = null;
          }
        });

        svg.appendChild(circle);
      });
    });

    // Legend
    const legend = document.createElement('div');
    legend.style.display = 'flex';
    legend.style.justifyContent = 'center';
    legend.style.gap = '1.5rem';
    legend.style.marginTop = '1rem';
    legend.style.fontSize = '0.875rem';

    metrics.forEach(metric => {
      if (!data.some(d => d[metric.key] > 0)) return;

      const item = document.createElement('div');
      item.style.display = 'flex';
      item.style.alignItems = 'center';
      item.style.gap = '0.5rem';

      const dot = document.createElement('div');
      dot.style.width = '12px';
      dot.style.height = '12px';
      dot.style.backgroundColor = metric.color;
      dot.style.borderRadius = '50%';

      const label = document.createElement('span');
      label.textContent = metric.label;
      label.style.color = '#374151';

      item.appendChild(dot);
      item.appendChild(label);
      legend.appendChild(item);
    });

    container.appendChild(svg);
    container.appendChild(legend);

  }, [engagementTrends]);

  if (!engagementTrends || Object.keys(engagementTrends).length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
        No engagement trends data available
      </div>
    );
  }

  return (
    <div>
      <div ref={containerRef} style={{ padding: '1rem' }} />
    </div>
  );
};

export default EngagementTrends; 