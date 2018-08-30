import { SEARCH_FAILED, SEARCH_PENDING, SEARCH_SUCCESS } from './actionTypes';
import * as api from './api';

export const searchPending = () => ({
  type: SEARCH_PENDING,
});

export const searchSuccess = (data) => ({
  type: SEARCH_SUCCESS,
  payload: {
    data,
  },
});

export const searchFailed = (error) => ({
  type: SEARCH_FAILED,
  payload: {
    error,
  },
});

export const search = image => dispatch => {
  dispatch(searchPending());

  return api.search(image)
    .then(response => {
      dispatch(searchSuccess(response));
    })
    .catch(e => {
      dispatch(searchFailed(e));
    });
};
