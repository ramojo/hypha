import React from 'react';
import PropTypes from 'prop-types';

import LoadingPanel from '@components/LoadingPanel';
import InlineLoading from '@components/InlineLoading';
import EmptyPanel from '@components/EmptyPanel';

import SadNoteIcon from 'images/sad-note.svg';

import './style.scss';

export default class Listing extends React.Component {
    static propTypes = {
        items: PropTypes.array.isRequired,
        isLoading: PropTypes.bool,
        isErrored: PropTypes.bool,
        errorMessage: PropTypes.string,
        groupBy: PropTypes.string,
        order: PropTypes.arrayOf(PropTypes.string),
        onItemSelection: PropTypes.func,
        renderItem: PropTypes.func.isRequired,
        handleRetry: PropTypes.func,
        listRef: PropTypes.object,
        column: PropTypes.string
    };

    renderListItems() {
        const {
            isErrored,
            items,
            renderItem
        } = this.props;

        return (
            <>
                { isErrored && this.renderErrorItem() }
                {items.map(v => renderItem(v))}
            </>
        );
    }

    renderRetryButton = () => {
        const {handleRetry} = this.props;
        return <a className="listing__help-link" onClick={handleRetry}>Refresh</a>;
    };

    renderErrorItem = () => {
        const {handleRetry, errorMessage} = this.props;
        return (
            <li className="listing__item listing__item--error">
                <h5>Something went wrong!</h5>
                <p>{errorMessage}</p>
                { !navigator.onLine && <p>You appear to be offline.</p>}
                { handleRetry && this.renderRetryButton() }
            </li>
        );
    };

    renderError = () => {
        const {handleRetry, isErrored, errorMessage, column} = this.props;

        return (
            <div className={`listing listing--${column} is-blank`}>
                {isErrored && <p>{errorMessage}</p>}

                {!handleRetry &&
                    <p>Something went wrong!</p>
                }

                {handleRetry &&
                    <>
                        <div className="listing__blank-icon">
                            <SadNoteIcon />
                        </div>
                        <p className="listing__help-text listing__help-text--standout">Something went wrong!</p>
                        <p className="listing__help-text">Sorry we couldn&apos;t load the notes</p>
                        { this.renderRetryButton() }
                    </>
                }
            </div>
        );
    };

    render() {
        const {
            isErrored,
            isLoading,
            items,
            column,
            listRef
        } = this.props;

        if (items.length === 0) {
            if (isLoading) {
                return (
                    <LoadingPanel />
                );
            }
            else if (isErrored) {
                return this.renderError();
            }
            else {
                return <EmptyPanel column={this.props.column} />;
            }
        }

        return (
            <>
                { isLoading && <InlineLoading /> }
                <ul className={`listing listing--${column}`} ref={listRef}>
                    {this.renderListItems()}
                </ul>
            </>
        );
    }
}
