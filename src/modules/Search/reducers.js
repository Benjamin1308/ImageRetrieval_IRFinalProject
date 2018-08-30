import {SEARCH_FAILED, SEARCH_PENDING, SEARCH_SUCCESS} from './actionTypes';

const INITIAL_STATE = {
  data: [],
  pending: false,
  error: '',
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case SEARCH_PENDING: {
      return { ...INITIAL_STATE, pending: true };
    }
    case SEARCH_SUCCESS: {
      return { ...INITIAL_STATE, data: action.payload.data };
    }
    case SEARCH_FAILED: {
      return { ...INITIAL_STATE, error: action.payload.error };
    }
    default: {
      return state;
    }
  }
};
