// import React from 'react';
import Markdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { dark } from 'react-syntax-highlighter/dist/esm/styles/prism';

const ResFormatter = ({ txt }) => {
  // You can customize the rendering as needed by providing a custom renderer
  // or using additional props for `Markdown` component here.
  console.log(txt);
  return (
    <>
      {/* <Markdown>{txt}</Markdown> */}
      <Markdown
        children={txt}
        components={{
          code(props) {
            const { children, className, node, ...rest } = props;
            const match = /language-(\w+)/.exec(className || '');
            return match ? (
              <SyntaxHighlighter
                {...rest}
                children={String(children).replace(/\n$/, '')}
                style={dark}
                language={match[1]}
                PreTag='div'
              />
            ) : (
              <code {...rest} className={className}>
                {children}
              </code>
            );
          },
          li(props) {
            return <li {...props} style={{ margin: '20px 0' }} />;
          },
          a(props) {
            return (
              <a {...props} style={{ color: 'royalblue' }} target='_blank' />
            );
          },
        }}
      />
    </>
  );
};

export default ResFormatter;
