import React from 'react';

const WaveShapeDivider = ({ bottomColor = '#000', topColor = '#fff', }) => {
  const wrapperStyles = {
    backgroundColor: topColor,
  }

  const topStyles = {
    backgroundImage: `radial-gradient(
      circle at 10px -5px,
      transparent 12px,
      ${bottomColor} 13px)`, 
  }

  const bottomStyles = {
    backgroundImage: `radial-gradient(
      circle at 10px 15px,
      ${bottomColor} 12px,
      transparent 13px)`, 
  }

  return (
    <div className="shape__wave" style={ wrapperStyles }>
      <div className="wave_shape_1" style={ topStyles } />
      <div className="wave_shape_2" style={ bottomStyles } />
    </div>
  )
}

export default WaveShapeDivider;