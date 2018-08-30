import React, { Component } from 'react';
import { connect } from 'react-redux';
import { GridList, GridListTile, LinearProgress } from '@material-ui/core';
import uuid_v4 from 'uuid/v4';
import PropTypes from 'prop-types';

import {placeholder} from "../../../constants/mock/images";

class ImageGrid extends Component {
  renderImages() {
    const { images, pending, cols } = this.props;

    if (!pending) {
      return images.map(image =>
        <GridListTile key={uuid_v4()}>
          <img src={image} alt="similar" />
        </GridListTile>
      );
    }

    return [...Array(cols).keys()].map(() =>
      <GridListTile key={uuid_v4()}>
        <img src={placeholder} alt="loading" />
      </GridListTile>
    );
  }

  render() {
    const { cols, pending } = this.props;

    return (
      <div style={{ flexGrow: 1 }}>
        <GridList cols={cols} cellHeight={300}>
          {this.renderImages()}
        </GridList>
        {pending ? <LinearProgress/> : null}
      </div>
    );
  }
}

ImageGrid.propTypes = {
  images: PropTypes.arrayOf(PropTypes.string),
  cols: PropTypes.number,
  pending: PropTypes.bool,
};

ImageGrid.defaultProps = {
  images: [],
  cols: 2,
  pending: false,
};

const mapStateToProps = state => ({
  images: state.search.data,
  pending: state.search.pending,
});

export default connect(mapStateToProps)(ImageGrid);
