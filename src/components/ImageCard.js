import React from 'react';
import { Card, CardMedia, CardContent, Typography } from '@material-ui/core';
import PropTypes from 'prop-types';

const ImageCard = ({ src, description, label }) => (
  <Card style={{ width: 400 }}>
    <CardMedia
      image={src}
      title={description}
      style={{ height: 200 }}
    />

    {label ? <CardContent>
      <Typography variant="headline" gutterBottom>{label}</Typography>
    </CardContent> : null}

  </Card>
);

ImageCard.propTypes = {
  src: PropTypes.string,
  description: PropTypes.string,
  label: PropTypes.string,
};

ImageCard.defaultProps = {
  src: '',
  description: 'Card',
  label: '',
};

export default ImageCard;
