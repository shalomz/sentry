import React from 'react';
import PropTypes from 'prop-types';
import styled from 'react-emotion';
import {Flex, Box} from 'grid-emotion';

import Button from 'app/components/buttons/button';
import {t} from 'app/locale';

export default class Deploys extends React.Component {
  static propTypes = {
    deploys: PropTypes.object,
  };
  render() {
    return <NoDeploys />;
  }
}

class NoDeploys extends React.Component {
  render() {
    return (
      <Box p={1}>
        <Background align="center" justify="center" p={1}>
          <Button size="xsmall">{t('Track deploys')}</Button>
        </Background>
      </Box>
    );
  }
}

const Background = styled(Flex)`
  height: 64px;
  background-color: ${p => p.theme.offWhite};
`;
