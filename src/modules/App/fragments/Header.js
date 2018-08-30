import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Grid, Typography, Button, Icon } from '@material-ui/core';
import { encodeToBase64 } from '../../../utils/encoder';
import ImageCard from '../../../components/ImageCard';
import { placeholder } from '../../../constants/mock/images';
import {search} from '../../Search/actions';

class Header extends Component {
  state = {
    uploadedImagePath: 'Your image here',
    uploadedImage: placeholder,
    uploaded: false,
  };

  handleChooseImage() {
    setTimeout(() => {
      this.upload.click();
    }, 200);
  }

  handleReceiveImage(event) {
    if (typeof event.target.files[0] !== 'undefined') {
      this.setState({ uploadedImagePath: event.target.files[0].name });
      encodeToBase64(
        event.target.files[0],
        base64 => this.setState({ uploadedImage: base64, uploaded: true }),
        err => console.log(err)
      );
    }
  }

  handleSearch() {
    this.props.searchAction(this.state.uploadedImage.replace('data:image/png;base64,', ''));
  }

  render() {
    const { uploadedImage, uploadedImagePath, uploaded } = this.state;
    const { pending } = this.props;

    return (
      <React.Fragment>
        <Typography variant="display3">
          Find similar images to
        </Typography>

        <ImageCard src={uploadedImage} description="Uploaded" label={uploadedImagePath}/>

        <span style={{ padding: '10px' }} />

        <Grid
          container
          direction="row"
          justify="center"
          alignItems="center"
        >
          <input
            style={{ display: 'none' }}
            type="file"
            id="image_upload"
            accept="image/png, image/jpeg"
            onChange={this.handleReceiveImage.bind(this)}
          />
          <label htmlFor="image_upload" ref={ref => { this.upload = ref }}>
            <Button disabled={pending} variant="raised" color="default" onClick={this.handleChooseImage.bind(this)}>
              Upload&nbsp;&nbsp;
              <Icon>backup</Icon>
            </Button>
          </label>

          <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>

          <Button disabled={!uploaded || pending} variant="raised" color="primary" onClick={this.handleSearch.bind(this)}>
            Search&nbsp;&nbsp;
            <Icon>search</Icon>
          </Button>
        </Grid>
      </React.Fragment>
    );
  }
}

const mapStateToProps = state => ({
  pending: state.search.pending,
});

export default connect(mapStateToProps, { searchAction: search })(Header);
