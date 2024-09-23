from reflex import Reflex, Component, html
import requests

class BlockExplorer(Component):
    def render(self):
            blocks = self.get_blocks()
                    return html.div(
                                [html.h1("Block Explorer")] +
                                            [html.div(f"Block {block['index']}: {block['data']}") for block in blocks]
                                                    )

                                                        def get_blocks(self):
                                                                response = requests.get('http://localhost:5000/blocks')
                                                                        return response.json()

                                                                        class ValidationStatus(Component):
                                                                            def render(self):
                                                                                    is_valid = self.get_validation_status()
                                                                                            return html.div(
                                                                                                        [html.h1("Validation Status"), html.p(f"Blockchain is {'valid' if is_valid else 'invalid'}")]
                                                                                                                )

                                                                                                                    def get_validation_status(self):
                                                                                                                            response = requests.get('http://localhost:5000/validate_chain')
                                                                                                                                    return response.json()['is_valid']

                                                                                                                                    app = Reflex()
                                                                                                                                    app.add_route('/', BlockExplorer)
                                                                                                                                    app.add_route('/validate', ValidationStatus)

                                                                                                                                    if __name__ == '__main__':
                                                                                                                                        app.run()
                                                                                                                                        