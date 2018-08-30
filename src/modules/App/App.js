import React, { Component } from 'react';
import { Grid } from '@material-ui/core';
import Header from './fragments/Header';
import ImageGrid from './fragments/ImageGrid';

class App extends Component {
  render() {
    return (
      <Grid
        container
        direction="column"
        justify="center"
        alignItems="center"
      >
        <Header/>

        <div style={{ padding: '10px' }} />

        <ImageGrid cols={3} />
      </Grid>
    );
  }
}

export default App;
