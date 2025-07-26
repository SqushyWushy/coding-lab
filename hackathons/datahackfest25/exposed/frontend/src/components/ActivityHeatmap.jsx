import { useEffect, useRef } from 'react';

const ActivityHeatmap = ({ dailyActivity }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!dailyActivity || Object.keys(dailyActivity).length === 0) return;

    const container = containerRef.current;
    container.innerHTML = '';

    // Get date range
    const dates = Object.keys(dailyActivity).sort();
    if (dates.length === 0) return;

    const startDate = new Date(dates[0]);
    const endDate = new Date(dates[dates.length - 1]);
    
    // Calculate weeks needed
    const msPerDay = 24 * 60 * 60 * 1000;
    const daysBetween = Math.ceil((endDate - startDate) / msPerDay) + 1;
    const weeksNeeded = Math.ceil(daysBetween / 7);

    // Get max activity for color scaling
    const maxActivity = Math.max(...Object.values(dailyActivity));

    // Create grid container
    const grid = document.createElement('div');
    grid.style.display = 'grid';
    grid.style.gridTemplateColumns = 'repeat(53, 12px)';
    grid.style.gap = '2px';
    grid.style.justifyContent = 'center';

    // Generate all days
    const currentDate = new Date(startDate);
    currentDate.setDate(currentDate.getDate() - currentDate.getDay()); // Start from Sunday

    for (let week = 0; week < Math.min(weeksNeeded + 2, 53); week++) {
      for (let day = 0; day < 7; day++) {
        const dateKey = currentDate.toISOString().split('T')[0];
        const activity = dailyActivity[dateKey] || 0;
        
        const cell = document.createElement('div');
        cell.style.width = '12px';
        cell.style.height = '12px';
        cell.style.borderRadius = '2px';
        cell.style.cursor = 'pointer';
        
        // Color intensity based on activity
        let backgroundColor;
        if (activity === 0) {
          backgroundColor = '#f3f4f6';
        } else {
          const intensity = Math.min(activity / maxActivity, 1);
          if (intensity <= 0.2) backgroundColor = '#dbeafe';
          else if (intensity <= 0.4) backgroundColor = '#93c5fd';
          else if (intensity <= 0.6) backgroundColor = '#60a5fa';
          else if (intensity <= 0.8) backgroundColor = '#3b82f6';
          else backgroundColor = '#1d4ed8';
        }
        
        cell.style.backgroundColor = backgroundColor;
        
        // Tooltip
        cell.title = `${dateKey}: ${activity} videos watched`;
        
        // Hover effect
        cell.addEventListener('mouseenter', () => {
          cell.style.transform = 'scale(1.2)';
          cell.style.zIndex = '10';
          cell.style.position = 'relative';
        });
        
        cell.addEventListener('mouseleave', () => {
          cell.style.transform = 'scale(1)';
          cell.style.zIndex = 'auto';
          cell.style.position = 'static';
        });

        grid.appendChild(cell);
        currentDate.setDate(currentDate.getDate() + 1);
      }
    }

    container.appendChild(grid);

    // Add legend
    const legend = document.createElement('div');
    legend.style.display = 'flex';
    legend.style.alignItems = 'center';
    legend.style.justifyContent = 'center';
    legend.style.marginTop = '12px';
    legend.style.fontSize = '12px';
    legend.style.color = '#6b7280';
    legend.style.gap = '8px';

    legend.innerHTML = `
      <span>Less</span>
      <div style="width: 10px; height: 10px; background: #f3f4f6; border-radius: 2px;"></div>
      <div style="width: 10px; height: 10px; background: #dbeafe; border-radius: 2px;"></div>
      <div style="width: 10px; height: 10px; background: #93c5fd; border-radius: 2px;"></div>
      <div style="width: 10px; height: 10px; background: #60a5fa; border-radius: 2px;"></div>
      <div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 2px;"></div>
      <div style="width: 10px; height: 10px; background: #1d4ed8; border-radius: 2px;"></div>
      <span>More</span>
    `;

    container.appendChild(legend);

  }, [dailyActivity]);

  if (!dailyActivity || Object.keys(dailyActivity).length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
        No daily activity data available
      </div>
    );
  }

  return (
    <div>
      <div ref={containerRef} style={{ padding: '1rem' }} />
    </div>
  );
};

export default ActivityHeatmap; 